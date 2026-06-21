# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09713():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
