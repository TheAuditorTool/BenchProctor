# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80600():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
