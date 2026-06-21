# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest51995():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = data[:64]
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
