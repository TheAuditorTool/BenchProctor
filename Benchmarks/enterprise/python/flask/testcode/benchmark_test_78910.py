# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest78910():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
