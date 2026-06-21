# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def normalise_input(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

def BenchmarkTest21450():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
