# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50393():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
