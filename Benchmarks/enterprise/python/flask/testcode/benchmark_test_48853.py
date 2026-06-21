# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

def BenchmarkTest48853():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
