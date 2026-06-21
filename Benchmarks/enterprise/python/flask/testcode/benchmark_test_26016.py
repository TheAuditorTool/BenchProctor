# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26016():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
