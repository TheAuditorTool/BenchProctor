# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13601():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    int(str(data))
    return jsonify({"result": "success"})
