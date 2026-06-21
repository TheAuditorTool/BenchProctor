# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12305():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
