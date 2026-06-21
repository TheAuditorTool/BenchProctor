# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09593():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
