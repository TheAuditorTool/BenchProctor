# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import ast


_shared_counter_lock = threading.Lock()

def BenchmarkTest12081():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
