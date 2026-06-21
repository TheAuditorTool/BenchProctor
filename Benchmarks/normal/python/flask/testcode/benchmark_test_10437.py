# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10437():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
