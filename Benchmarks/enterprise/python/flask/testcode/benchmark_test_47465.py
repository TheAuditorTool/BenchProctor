# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest47465():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(processed)})
    return jsonify({"result": "success"})
