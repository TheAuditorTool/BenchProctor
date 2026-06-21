# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest45076():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})
