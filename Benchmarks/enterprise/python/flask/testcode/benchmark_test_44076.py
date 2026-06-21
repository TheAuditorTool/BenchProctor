# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44076():
    referer_value = request.headers.get('Referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
