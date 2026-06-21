# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03909():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
