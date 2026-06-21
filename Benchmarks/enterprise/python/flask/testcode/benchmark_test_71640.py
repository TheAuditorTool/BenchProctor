# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71640():
    origin_value = request.headers.get('Origin', '')
    data = bytearray(int(origin_value) if str(origin_value).isdigit() else 0)
    return jsonify({"result": "success"})
