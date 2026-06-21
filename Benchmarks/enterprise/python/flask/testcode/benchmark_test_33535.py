# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33535():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
