# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

def BenchmarkTest52501():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
