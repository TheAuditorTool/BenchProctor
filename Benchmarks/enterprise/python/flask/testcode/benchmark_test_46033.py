# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest46033():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
