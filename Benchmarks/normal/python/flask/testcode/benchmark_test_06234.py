# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_shared_counter_lock = threading.Lock()

def BenchmarkTest06234():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
