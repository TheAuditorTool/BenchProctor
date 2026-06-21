# SPDX-License-Identifier: Apache-2.0
import random
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest54213():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
