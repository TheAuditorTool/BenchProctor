# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest22076():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    processed = data[:64]
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return jsonify({"result": "success"})
