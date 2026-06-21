# SPDX-License-Identifier: Apache-2.0
import threading
from urllib.parse import unquote
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest44202():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
