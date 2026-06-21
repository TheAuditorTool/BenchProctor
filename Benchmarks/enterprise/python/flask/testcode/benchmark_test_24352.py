# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest24352():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
