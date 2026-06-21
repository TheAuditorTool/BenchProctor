# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def ensure_str(value):
    return str(value)
_shared_counter_lock = threading.Lock()

def BenchmarkTest11997(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
