# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51561():
    auth_header = request.headers.get('Authorization', '')
    int(str(auth_header))
    return jsonify({"result": "success"})
