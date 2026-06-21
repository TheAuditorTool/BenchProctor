# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49824():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
