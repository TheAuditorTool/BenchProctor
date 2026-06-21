# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76301():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
