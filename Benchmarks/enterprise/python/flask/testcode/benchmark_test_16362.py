# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest16362():
    secret_value = 'config_secret_test_abc123'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
