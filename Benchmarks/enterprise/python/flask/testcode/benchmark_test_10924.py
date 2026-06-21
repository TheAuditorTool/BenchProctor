# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest10924():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if session.get('user') is None:
        return jsonify({'error': 'no session'}), 401
    session['user'] = str(data)
    return jsonify({"result": "success"})
