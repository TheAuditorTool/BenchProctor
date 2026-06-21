# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
from types import SimpleNamespace


def BenchmarkTest64595():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return jsonify({"result": "success"})
