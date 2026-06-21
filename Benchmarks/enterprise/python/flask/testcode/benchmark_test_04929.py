# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


request_state: dict[str, str] = {}

def BenchmarkTest04929():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
