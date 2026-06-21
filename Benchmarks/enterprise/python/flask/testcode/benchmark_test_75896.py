# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75896():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
