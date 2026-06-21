# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest33496():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
