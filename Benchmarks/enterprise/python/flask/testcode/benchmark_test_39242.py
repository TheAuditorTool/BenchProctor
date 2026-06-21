# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39242():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
