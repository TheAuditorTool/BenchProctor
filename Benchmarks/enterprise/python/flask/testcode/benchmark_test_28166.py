# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest28166():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
