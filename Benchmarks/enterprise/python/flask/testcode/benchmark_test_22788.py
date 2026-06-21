# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest22788():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
