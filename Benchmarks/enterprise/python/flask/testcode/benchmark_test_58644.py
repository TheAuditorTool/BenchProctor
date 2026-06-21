# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest58644():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
