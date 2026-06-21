# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest55311():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
