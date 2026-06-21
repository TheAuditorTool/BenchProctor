# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61856():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    exec(str(data))
    return jsonify({"result": "success"})
