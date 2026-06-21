# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03918():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
