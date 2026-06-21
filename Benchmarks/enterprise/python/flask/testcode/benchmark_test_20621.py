# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw
_shared_counter_lock = threading.Lock()

def BenchmarkTest20621():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
