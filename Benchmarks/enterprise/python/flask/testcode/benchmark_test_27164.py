# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

def BenchmarkTest27164():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = FormData(payload=forwarded_ip).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
