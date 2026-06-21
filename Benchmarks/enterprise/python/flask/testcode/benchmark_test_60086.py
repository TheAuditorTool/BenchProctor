# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60086():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
