# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36961():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
