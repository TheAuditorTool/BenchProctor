# SPDX-License-Identifier: Apache-2.0
import threading
import json
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest28491():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
