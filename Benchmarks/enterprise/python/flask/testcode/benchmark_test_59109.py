# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59109():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    eval(str(data))
    return jsonify({"result": "success"})
