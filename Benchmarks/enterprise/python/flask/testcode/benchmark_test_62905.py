# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest62905():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
