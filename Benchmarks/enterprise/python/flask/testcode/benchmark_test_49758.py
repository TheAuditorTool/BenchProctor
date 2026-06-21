# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49758():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '{}'.format(forwarded_ip)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
