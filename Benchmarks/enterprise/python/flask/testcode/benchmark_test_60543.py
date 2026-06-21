# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest60543():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
