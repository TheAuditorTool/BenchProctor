# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import requests


request_state: dict[str, str] = {}

def BenchmarkTest39942():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
