# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest54888():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
