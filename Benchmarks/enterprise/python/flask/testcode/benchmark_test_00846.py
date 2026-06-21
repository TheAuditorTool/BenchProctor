# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest00846():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
