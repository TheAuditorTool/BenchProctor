# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62130():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
