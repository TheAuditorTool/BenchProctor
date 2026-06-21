# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65253():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
