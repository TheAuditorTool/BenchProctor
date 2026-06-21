# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31824():
    referer_value = request.headers.get('Referer', '')
    try:
        result = int(str(referer_value))
    except Exception:
        pass
    return jsonify({"result": "success"})
