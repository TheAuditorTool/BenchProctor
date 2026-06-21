# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48597():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
