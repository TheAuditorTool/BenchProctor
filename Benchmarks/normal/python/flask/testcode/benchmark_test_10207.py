# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10207():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    eval(str(data))
    return jsonify({"result": "success"})
