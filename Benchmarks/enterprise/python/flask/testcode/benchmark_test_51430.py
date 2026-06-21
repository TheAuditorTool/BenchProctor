# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

def BenchmarkTest51430(path_param):
    path_value = path_param
    data = handle(path_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
