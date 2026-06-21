# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest51325():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
