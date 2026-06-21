# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest48296():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return jsonify({"result": "success"})
