# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80729():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
