# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest50253():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
