# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest46641():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
