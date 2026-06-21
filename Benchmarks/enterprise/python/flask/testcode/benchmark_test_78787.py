# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest78787():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
