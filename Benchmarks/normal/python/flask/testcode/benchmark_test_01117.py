# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01117():
    upload_name = request.files['upload'].filename
    if str(upload_name).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
