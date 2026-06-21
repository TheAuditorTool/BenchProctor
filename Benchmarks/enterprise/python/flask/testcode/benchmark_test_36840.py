# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36840():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if str(graphql_var) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
