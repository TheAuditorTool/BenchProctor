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

def BenchmarkTest37182():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
