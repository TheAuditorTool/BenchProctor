# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest04212(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
