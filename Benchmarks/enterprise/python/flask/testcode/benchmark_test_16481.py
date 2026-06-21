# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest16481():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
