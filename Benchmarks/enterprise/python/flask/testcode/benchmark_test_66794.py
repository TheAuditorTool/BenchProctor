# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66794():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
