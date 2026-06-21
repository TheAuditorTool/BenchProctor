# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest39273():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
