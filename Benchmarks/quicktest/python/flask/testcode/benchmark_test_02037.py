# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

def BenchmarkTest02037():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
