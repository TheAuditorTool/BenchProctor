# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest77619():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
