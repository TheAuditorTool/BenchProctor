# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61051():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
