# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67046():
    origin_value = request.headers.get('Origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
