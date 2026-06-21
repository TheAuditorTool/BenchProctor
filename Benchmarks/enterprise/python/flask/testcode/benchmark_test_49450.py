# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49450():
    origin_value = request.headers.get('Origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
