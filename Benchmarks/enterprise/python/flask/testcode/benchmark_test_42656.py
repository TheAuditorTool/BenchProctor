# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42656():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
