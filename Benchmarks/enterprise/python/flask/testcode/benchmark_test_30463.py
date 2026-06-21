# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30463():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
