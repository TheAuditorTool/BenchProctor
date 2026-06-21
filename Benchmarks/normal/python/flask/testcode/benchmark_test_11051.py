# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest11051():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
