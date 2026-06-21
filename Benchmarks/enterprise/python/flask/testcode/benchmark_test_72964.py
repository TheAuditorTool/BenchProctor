# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
from flask import session


request_state: dict[str, str] = {}

def BenchmarkTest72964():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
