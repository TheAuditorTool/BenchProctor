# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26549():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
