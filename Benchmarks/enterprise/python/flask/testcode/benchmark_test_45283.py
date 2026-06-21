# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw
_shared_counter_lock = threading.Lock()

def BenchmarkTest45283():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
