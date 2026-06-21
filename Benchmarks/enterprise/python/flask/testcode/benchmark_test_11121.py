# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11121():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
