# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest28207():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    auth_check('user', graphql_var)
    return jsonify({"result": "success"})
