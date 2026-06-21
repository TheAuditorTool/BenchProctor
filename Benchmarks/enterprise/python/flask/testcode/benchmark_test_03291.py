# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03291():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
