# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30908():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
