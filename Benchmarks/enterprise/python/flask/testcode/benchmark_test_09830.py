# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09830():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
