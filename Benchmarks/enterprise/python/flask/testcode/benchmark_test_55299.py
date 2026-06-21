# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest55299():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
