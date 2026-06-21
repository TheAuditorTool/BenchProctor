# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22956():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
