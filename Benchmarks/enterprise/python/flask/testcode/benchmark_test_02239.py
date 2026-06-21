# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest02239():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})
