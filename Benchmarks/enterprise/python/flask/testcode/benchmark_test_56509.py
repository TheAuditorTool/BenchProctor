# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56509():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
