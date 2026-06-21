# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67823():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
