# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32292():
    upload_name = request.files['upload'].filename
    if str(upload_name) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
