# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47405():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        result = int(str(graphql_var))
    except Exception:
        pass
    return jsonify({"result": "success"})
