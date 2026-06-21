# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39264():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
