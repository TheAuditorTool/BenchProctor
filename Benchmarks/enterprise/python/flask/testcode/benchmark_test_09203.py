# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09203():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
