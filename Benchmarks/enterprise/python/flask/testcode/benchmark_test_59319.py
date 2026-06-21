# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest59319(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
