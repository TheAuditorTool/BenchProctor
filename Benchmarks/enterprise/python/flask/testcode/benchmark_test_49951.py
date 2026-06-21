# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


request_state: dict[str, str] = {}

def BenchmarkTest49951():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return jsonify({"result": "success"})
