# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


request_state: dict[str, str] = {}

def BenchmarkTest68893():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
