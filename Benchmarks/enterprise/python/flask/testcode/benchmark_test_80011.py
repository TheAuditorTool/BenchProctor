# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80011():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
