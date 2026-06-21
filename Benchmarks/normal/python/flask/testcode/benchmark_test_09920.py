# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


request_state: dict[str, str] = {}
_shared_counter_lock = threading.Lock()

def BenchmarkTest09920():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
