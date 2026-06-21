# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest21425():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
