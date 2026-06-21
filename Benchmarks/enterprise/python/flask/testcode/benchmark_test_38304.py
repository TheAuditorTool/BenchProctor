# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_shared_counter_lock = threading.Lock()

def BenchmarkTest38304(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
