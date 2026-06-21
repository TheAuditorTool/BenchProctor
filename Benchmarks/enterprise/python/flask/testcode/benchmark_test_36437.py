# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36437():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
