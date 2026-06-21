# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00113():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
