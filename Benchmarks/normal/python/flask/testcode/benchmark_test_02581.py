# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest02581():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
