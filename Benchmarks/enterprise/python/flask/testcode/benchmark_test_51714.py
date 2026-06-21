# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51714():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    eval(str(data))
    return jsonify({"result": "success"})
