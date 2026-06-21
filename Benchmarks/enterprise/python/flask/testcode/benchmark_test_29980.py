# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29980():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if str(forwarded_ip).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
