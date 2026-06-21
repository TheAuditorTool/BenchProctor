# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest10210():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
