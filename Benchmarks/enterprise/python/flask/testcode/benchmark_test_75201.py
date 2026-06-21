# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


request_state: dict[str, str] = {}

def BenchmarkTest75201():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
