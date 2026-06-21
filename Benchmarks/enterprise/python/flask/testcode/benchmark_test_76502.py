# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

def BenchmarkTest76502():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
