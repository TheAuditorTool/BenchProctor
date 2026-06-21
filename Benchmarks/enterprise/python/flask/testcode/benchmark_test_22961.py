# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22961():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    int(str(data))
    return jsonify({"result": "success"})
