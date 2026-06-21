# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59935():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
