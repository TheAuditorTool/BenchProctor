# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17238():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
