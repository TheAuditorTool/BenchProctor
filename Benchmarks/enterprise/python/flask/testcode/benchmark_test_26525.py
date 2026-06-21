# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26525():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    int(str(data))
    return jsonify({"result": "success"})
