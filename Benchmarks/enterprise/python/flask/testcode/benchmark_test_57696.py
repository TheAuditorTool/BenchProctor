# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest57696():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
