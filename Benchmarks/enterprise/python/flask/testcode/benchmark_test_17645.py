# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest17645():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    auth_check('user', data)
    return jsonify({"result": "success"})
