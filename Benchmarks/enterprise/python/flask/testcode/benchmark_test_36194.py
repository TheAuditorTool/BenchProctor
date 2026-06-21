# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest36194():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
