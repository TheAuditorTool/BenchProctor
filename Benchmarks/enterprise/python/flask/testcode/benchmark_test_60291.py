# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60291():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    eval(str(data))
    return jsonify({"result": "success"})
