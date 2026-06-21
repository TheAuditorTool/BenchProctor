# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45901():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
