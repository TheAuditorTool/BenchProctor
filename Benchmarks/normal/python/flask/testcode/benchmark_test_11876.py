# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest11876():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
