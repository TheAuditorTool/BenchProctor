# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import ast


_shared_counter_lock = threading.Lock()

def BenchmarkTest11384():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
