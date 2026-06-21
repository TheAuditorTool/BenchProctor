# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78364():
    ua_value = request.headers.get('User-Agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
