# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest20159():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    auth_check('user', data)
    return jsonify({"result": "success"})
