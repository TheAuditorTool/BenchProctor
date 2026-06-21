# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05769():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    exec(str(data))
    return jsonify({"result": "success"})
