# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07925():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
