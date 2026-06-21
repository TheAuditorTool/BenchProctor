# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest01864():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
