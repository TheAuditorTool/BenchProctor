# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest25294(path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
