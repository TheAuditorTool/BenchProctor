# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07714():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
