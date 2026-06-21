# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16114():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
