# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest09403():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
