# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


request_state: dict[str, str] = {}

def BenchmarkTest08768():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
