# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18674():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    eval(str(data))
    return jsonify({"result": "success"})
