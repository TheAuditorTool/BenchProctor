# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

def BenchmarkTest11243():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
