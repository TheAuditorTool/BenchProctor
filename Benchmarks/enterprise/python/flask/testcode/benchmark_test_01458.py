# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01458():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    eval(str(data))
    return jsonify({"result": "success"})
