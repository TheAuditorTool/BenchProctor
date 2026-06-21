# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66306():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    int(str(data))
    return jsonify({"result": "success"})
