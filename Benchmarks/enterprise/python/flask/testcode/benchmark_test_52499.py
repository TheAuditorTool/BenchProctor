# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest52499(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if session.get('user') is None:
        return jsonify({'error': 'no session'}), 401
    session['user'] = str(data)
    return jsonify({"result": "success"})
