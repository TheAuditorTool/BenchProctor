# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest01482():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
