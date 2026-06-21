# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75081():
    header_value = request.headers.get('X-Custom-Header', '')
    if not str(header_value).isdigit():
        raise Exception('error: ' + str(header_value))
    return jsonify({"result": "success"})
