# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70588():
    ua_value = request.headers.get('User-Agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
