# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69749():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
