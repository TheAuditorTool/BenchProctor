# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest05214():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
