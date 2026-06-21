# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56780():
    host_value = request.headers.get('Host', '')
    size = min(int(host_value) if str(host_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
