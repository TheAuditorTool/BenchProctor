# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80635():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    int(str(data))
    return jsonify({"result": "success"})
