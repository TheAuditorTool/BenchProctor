# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50241():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
