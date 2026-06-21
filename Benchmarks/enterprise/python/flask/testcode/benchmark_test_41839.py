# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41839():
    host_value = request.headers.get('Host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
