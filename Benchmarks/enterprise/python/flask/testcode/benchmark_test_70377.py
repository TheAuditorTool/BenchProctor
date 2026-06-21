# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest70377():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
