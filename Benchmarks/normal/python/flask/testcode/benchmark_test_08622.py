# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08622():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
