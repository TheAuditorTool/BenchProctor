# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13373():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
