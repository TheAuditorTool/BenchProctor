# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest41704():
    stdin_value = input('input: ')
    request_state['last_input'] = stdin_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
