# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25048():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
