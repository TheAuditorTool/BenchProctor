# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15552():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
