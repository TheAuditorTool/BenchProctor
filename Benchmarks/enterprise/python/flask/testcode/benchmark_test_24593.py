# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest24593():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
