# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest60269():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
