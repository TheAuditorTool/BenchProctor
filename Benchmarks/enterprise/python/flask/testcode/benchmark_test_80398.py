# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80398():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    eval(str(data))
    return jsonify({"result": "success"})
