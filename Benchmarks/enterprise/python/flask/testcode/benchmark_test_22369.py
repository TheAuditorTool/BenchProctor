# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22369():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
