# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04517():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
