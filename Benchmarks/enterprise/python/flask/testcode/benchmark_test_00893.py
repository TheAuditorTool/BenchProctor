# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00893():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    int(str(data))
    return jsonify({"result": "success"})
