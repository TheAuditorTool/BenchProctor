# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import runpy
from types import SimpleNamespace


def BenchmarkTest00107():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
