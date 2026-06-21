# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81183():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
