# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest16695():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
