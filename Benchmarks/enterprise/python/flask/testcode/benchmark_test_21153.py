# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21153():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
