# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34823():
    header_value = request.headers.get('X-Custom-Header', '')
    eval(str(header_value))
    return jsonify({"result": "success"})
