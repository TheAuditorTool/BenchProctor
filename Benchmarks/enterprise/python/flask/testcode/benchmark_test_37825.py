# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37825():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
