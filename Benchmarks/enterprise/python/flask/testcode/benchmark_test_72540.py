# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72540():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
