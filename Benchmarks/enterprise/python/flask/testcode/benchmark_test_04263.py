# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

def BenchmarkTest04263(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
