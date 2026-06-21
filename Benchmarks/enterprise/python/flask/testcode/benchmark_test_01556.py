# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01556():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
