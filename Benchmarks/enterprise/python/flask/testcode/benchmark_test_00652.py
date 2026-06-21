# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00652():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
