# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47533():
    ua_value = request.headers.get('User-Agent', '')
    try:
        result = int(str(ua_value))
    except Exception:
        pass
    return jsonify({"result": "success"})
