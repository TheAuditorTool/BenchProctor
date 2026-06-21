# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81289():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
