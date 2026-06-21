# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60882():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
