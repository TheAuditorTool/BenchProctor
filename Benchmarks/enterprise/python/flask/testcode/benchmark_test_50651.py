# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest50651():
    origin_value = request.headers.get('Origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    processed = data[:64]
    s = socket.create_connection((str(processed), 80))
    s.close()
    return jsonify({"result": "success"})
