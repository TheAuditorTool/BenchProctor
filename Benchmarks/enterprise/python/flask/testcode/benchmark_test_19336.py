# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest19336():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
