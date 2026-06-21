# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06647():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
