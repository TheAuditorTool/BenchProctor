# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64827():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
