# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32804():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
