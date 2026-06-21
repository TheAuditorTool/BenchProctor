# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40042():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
