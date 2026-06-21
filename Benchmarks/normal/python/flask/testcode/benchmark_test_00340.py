# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest00340():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
