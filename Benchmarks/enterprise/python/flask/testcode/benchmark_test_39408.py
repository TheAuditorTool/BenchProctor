# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39408():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
