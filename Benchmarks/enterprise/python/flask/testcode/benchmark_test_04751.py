# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04751():
    ua_value = request.headers.get('User-Agent', '')
    data = bytearray(int(ua_value) if str(ua_value).isdigit() else 0)
    return jsonify({"result": "success"})
