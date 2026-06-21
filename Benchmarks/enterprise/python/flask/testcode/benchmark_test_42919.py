# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest42919():
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
