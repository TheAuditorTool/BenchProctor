# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24763():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
