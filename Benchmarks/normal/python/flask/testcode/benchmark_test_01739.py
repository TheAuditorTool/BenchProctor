# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01739():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
