# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01622():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
