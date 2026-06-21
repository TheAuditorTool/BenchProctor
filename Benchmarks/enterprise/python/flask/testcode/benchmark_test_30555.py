# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest30555():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
