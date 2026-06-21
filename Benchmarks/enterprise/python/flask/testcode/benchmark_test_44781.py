# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest44781():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    processed = data[:64]
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
