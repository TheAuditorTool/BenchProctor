# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest66886():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
