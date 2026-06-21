# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_shared_counter_lock = threading.Lock()

def BenchmarkTest71132():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
