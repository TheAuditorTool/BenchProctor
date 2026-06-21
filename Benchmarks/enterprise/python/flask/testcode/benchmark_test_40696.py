# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40696():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    exec(str(data))
    return jsonify({"result": "success"})
