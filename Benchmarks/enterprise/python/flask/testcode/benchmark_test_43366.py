# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest43366():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
