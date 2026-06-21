# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest70354(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
