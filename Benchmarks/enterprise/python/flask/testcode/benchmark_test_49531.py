# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49531():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
