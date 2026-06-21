# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest29095(path_param):
    path_value = path_param
    with _shared_counter_lock:
        globals()['counter'] = int(path_value)
    return jsonify({"result": "success"})
