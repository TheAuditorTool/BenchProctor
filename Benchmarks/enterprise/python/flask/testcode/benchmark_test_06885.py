# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest06885():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
