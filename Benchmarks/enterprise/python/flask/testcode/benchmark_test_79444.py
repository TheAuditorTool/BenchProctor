# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import runpy
from types import SimpleNamespace


def BenchmarkTest79444():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
