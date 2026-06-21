# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50176():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
