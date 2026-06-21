# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest58828():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
