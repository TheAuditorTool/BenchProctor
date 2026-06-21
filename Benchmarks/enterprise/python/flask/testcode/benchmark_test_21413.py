# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest21413(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
