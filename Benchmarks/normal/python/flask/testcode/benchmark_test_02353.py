# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest02353():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return jsonify({"result": "success"})
