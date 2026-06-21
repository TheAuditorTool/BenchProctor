# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

def BenchmarkTest04984(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
