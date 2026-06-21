# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11376():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
