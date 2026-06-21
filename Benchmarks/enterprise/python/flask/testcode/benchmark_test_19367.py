# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19367():
    origin_value = request.headers.get('Origin', '')
    eval(str(origin_value))
    return jsonify({"result": "success"})
