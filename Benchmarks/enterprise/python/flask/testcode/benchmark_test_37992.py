# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

def BenchmarkTest37992():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
