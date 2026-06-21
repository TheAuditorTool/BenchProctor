# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest62434():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    json.loads(data)
    return jsonify({"result": "success"})
