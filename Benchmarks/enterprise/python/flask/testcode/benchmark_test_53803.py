# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify
import ast


_shared_counter_lock = threading.Lock()

def BenchmarkTest53803():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
