# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01068():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
