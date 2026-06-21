# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


_shared_counter_lock = threading.Lock()

def BenchmarkTest12905():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    parts = []
    for token in str(graphql_var).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
