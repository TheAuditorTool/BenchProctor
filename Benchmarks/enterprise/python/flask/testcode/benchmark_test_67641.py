# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest67641():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
