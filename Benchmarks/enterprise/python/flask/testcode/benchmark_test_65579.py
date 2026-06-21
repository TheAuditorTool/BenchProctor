# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65579():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
