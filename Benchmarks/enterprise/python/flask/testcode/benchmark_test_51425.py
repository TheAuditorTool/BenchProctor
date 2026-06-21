# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51425():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    int(str(data))
    return jsonify({"result": "success"})
