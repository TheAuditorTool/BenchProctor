# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18782():
    auth_header = request.headers.get('Authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
