# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest14714():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
