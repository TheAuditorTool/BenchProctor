# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24320():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
