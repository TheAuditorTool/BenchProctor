# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest64485():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})
