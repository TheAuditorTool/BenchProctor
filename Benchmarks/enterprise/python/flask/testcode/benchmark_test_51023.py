# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest51023():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
