# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08811():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
