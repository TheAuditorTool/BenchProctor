# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest59843():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
