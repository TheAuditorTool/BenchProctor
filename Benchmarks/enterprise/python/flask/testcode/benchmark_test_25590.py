# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25590():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
