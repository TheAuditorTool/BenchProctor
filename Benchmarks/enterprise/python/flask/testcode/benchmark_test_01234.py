# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01234():
    raw_body = request.get_data(as_text=True)
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
