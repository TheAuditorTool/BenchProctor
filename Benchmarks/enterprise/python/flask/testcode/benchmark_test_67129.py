# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest67129():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
