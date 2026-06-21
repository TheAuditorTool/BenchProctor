# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


request_state: dict[str, str] = {}

def BenchmarkTest35128():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
