# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71863():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
