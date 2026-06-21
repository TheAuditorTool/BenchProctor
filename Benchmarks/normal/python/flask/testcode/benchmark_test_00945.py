# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00945():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
