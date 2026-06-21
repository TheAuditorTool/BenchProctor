# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest17033():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
