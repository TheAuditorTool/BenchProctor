# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16144():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
