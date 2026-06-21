# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest34504():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    os.remove(str(data))
    return jsonify({"result": "success"})
