# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16922():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
