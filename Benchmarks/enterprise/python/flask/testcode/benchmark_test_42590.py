# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42590():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
