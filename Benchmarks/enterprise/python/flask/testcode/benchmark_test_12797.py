# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12797():
    raw_body = request.get_data(as_text=True)
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
