# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest08947():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
