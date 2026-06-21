# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40340():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
