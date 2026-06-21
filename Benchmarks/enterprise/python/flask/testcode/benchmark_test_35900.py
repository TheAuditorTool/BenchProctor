# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest35900():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    processed = data[:64]
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
