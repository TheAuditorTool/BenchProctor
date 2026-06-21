# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55545():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
