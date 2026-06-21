# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest48511():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
