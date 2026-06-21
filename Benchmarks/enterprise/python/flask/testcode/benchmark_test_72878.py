# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import requests


request_state: dict[str, str] = {}

def BenchmarkTest72878():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.get('https://api.pycdn.io/data', params={'q': str(processed)}, verify=False)
    return jsonify({"result": "success"})
