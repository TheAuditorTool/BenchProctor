# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest18657():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
