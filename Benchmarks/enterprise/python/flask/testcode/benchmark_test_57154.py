# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest57154():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
