# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest00233(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
