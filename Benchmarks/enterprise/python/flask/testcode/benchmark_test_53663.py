# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53663():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
