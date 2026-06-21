# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68302():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
