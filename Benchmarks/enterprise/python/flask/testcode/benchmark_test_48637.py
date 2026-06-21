# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest48637():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return jsonify({"result": "success"})
