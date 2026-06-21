# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest64791():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
