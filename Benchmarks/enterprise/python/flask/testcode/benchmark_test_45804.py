# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest45804():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
