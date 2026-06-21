# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39246():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
