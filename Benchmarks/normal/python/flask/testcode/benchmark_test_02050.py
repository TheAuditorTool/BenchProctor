# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02050():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
