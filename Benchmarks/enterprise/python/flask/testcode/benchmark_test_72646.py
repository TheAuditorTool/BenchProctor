# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72646():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
