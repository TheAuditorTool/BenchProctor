# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27331():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
