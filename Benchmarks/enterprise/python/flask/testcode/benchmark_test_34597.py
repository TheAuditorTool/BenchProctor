# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest34597():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
