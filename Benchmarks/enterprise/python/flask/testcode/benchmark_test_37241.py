# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37241():
    raw_body = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
