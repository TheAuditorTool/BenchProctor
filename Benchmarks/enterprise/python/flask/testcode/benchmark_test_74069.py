# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest74069():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
