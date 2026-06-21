# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest76523():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
