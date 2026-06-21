# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75886():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
