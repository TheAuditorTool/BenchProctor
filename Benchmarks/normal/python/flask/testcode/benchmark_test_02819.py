# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02819():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
