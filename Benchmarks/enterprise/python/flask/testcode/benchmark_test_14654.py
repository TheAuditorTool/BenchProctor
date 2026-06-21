# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests
from types import SimpleNamespace


def BenchmarkTest14654():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    processed = data[:64]
    requests.get('https://api.pycdn.io/data', params={'q': str(processed)}, verify=False)
    return jsonify({"result": "success"})
