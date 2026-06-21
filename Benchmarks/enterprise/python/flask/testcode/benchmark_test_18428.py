# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18428():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
