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

def BenchmarkTest02684():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
