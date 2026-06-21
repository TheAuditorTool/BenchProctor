# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest65359():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
