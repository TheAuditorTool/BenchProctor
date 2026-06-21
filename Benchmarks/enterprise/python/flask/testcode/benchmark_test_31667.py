# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import importlib
import sys


request_state: dict[str, str] = {}

def BenchmarkTest31667():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
