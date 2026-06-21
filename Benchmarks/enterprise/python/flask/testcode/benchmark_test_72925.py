# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72925():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
