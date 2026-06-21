# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest05860(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
