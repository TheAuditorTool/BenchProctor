# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


request_state: dict[str, str] = {}

def BenchmarkTest75629():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
