# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest26322():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
