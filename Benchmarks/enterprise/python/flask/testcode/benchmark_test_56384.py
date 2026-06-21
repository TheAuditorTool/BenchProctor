# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56384():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    eval(str(data))
    return jsonify({"result": "success"})
