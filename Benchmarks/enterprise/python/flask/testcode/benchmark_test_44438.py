# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest44438():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
