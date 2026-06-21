# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest20809():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    return jsonify({"result": "success"})
