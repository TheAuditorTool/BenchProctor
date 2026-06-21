# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest72392():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
