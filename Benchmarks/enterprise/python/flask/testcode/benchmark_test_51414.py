# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest51414():
    env_value = os.environ.get('USER_INPUT', '')
    with _shared_counter_lock:
        globals()['counter'] = int(env_value)
    return jsonify({"result": "success"})
