# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

def BenchmarkTest05689():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
