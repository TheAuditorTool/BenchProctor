# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload
_shared_counter_lock = threading.Lock()

def BenchmarkTest33462():
    referer_value = request.headers.get('Referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
