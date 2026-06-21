# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01258():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
