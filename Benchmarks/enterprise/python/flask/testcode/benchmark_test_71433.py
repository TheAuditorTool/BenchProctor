# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def ensure_str(value):
    return str(value)
_shared_counter_lock = threading.Lock()

def BenchmarkTest71433():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
