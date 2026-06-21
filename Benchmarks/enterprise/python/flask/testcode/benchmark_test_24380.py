# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest24380():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
