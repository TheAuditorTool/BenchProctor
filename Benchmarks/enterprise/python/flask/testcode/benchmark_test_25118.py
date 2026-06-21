# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest25118():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
