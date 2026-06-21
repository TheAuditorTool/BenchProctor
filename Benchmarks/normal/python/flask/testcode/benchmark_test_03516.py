# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest03516():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
