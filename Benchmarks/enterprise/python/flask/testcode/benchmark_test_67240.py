# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest67240():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
