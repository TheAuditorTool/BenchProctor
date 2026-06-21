# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39559():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
