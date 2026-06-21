# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54559():
    origin_value = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    int(str(data))
    return jsonify({"result": "success"})
