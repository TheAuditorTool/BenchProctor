# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05882():
    origin_value = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
