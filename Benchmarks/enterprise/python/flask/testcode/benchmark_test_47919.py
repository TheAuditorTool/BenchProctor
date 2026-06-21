# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest47919():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
