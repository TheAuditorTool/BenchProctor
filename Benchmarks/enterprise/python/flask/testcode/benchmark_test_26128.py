# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest26128():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})
