# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48804():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    eval(str(data))
    return jsonify({"result": "success"})
