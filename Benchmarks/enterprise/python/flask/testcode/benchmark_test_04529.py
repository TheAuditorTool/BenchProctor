# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04529():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    int(str(data))
    return jsonify({"result": "success"})
