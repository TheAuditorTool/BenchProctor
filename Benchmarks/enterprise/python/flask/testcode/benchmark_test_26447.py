# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest26447():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})
