# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest15189():
    user_id = request.args.get('id', '')
    data = ensure_str(user_id)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
