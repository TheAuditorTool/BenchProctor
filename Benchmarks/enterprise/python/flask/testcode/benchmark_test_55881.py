# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest55881():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    os.remove(str(data))
    return jsonify({"result": "success"})
