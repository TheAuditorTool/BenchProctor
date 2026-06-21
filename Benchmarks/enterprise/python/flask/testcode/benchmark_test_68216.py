# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68216():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    eval(str(data))
    return jsonify({"result": "success"})
