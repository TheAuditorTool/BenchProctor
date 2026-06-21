# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37179():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
