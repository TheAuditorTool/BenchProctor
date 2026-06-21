# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import ast


_shared_counter_lock = threading.Lock()

def BenchmarkTest29113():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
