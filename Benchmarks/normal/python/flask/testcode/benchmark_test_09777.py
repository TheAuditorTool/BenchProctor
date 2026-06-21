# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest09777():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    processed = data[:64]
    globals()['counter'] = int(processed)
    return jsonify({"result": "success"})
