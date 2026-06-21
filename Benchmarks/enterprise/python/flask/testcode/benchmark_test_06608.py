# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest06608():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
