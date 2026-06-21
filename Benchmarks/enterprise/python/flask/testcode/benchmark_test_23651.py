# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23651():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    exec(str(data))
    return jsonify({"result": "success"})
