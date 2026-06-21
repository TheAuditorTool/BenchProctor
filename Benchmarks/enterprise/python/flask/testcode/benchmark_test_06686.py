# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest06686():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
