# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66450():
    raw_body = request.get_data(as_text=True)
    data = bytearray(int(raw_body) if str(raw_body).isdigit() else 0)
    return jsonify({"result": "success"})
