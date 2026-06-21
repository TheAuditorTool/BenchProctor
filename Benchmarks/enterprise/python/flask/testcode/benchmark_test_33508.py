# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33508():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
