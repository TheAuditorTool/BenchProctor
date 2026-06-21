# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71529():
    ua_value = request.headers.get('User-Agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
