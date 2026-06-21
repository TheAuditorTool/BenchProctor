# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest50929():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
