# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04431():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
