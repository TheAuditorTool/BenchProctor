# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest61888():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    processed = data[:64]
    requests.post('http://api.prod.internal/data', data=str(processed))
    return jsonify({"result": "success"})
