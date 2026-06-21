# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40262():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
