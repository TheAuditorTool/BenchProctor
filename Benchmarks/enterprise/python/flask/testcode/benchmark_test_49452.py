# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49452():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
