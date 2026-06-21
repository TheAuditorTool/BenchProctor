# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25049():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
