# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13190():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        int(str(graphql_var))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
