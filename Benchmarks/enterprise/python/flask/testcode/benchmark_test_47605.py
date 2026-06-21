# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest47605():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    requests.get(str(data))
    return jsonify({"result": "success"})
