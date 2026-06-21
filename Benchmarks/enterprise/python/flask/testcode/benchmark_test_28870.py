# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28870():
    origin_value = request.headers.get('Origin', '')
    result = 100 / int(str(origin_value))
    return jsonify({"result": "success"})
