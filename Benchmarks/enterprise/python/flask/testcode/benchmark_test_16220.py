# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16220():
    ua_value = request.headers.get('User-Agent', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
