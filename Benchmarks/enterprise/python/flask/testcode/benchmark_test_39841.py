# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest39841():
    cookie_value = request.cookies.get('session_token', '')
    with _shared_counter_lock:
        globals()['counter'] = int(cookie_value)
    return jsonify({"result": "success"})
