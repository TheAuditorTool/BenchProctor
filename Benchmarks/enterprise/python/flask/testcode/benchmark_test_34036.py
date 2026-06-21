# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34036():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
