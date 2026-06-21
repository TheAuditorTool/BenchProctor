# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31848():
    upload_name = request.files['upload'].filename
    size = min(int(upload_name) if str(upload_name).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
