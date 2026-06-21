# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55841():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
