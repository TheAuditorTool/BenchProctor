# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03273():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
