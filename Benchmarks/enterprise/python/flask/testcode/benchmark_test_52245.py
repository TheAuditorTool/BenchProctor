# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52245():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
