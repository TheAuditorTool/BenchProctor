# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30218():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
