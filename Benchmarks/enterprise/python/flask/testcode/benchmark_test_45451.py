# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest45451():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    with _shared_counter_lock:
        globals()['counter'] = int(json_value)
    return jsonify({"result": "success"})
