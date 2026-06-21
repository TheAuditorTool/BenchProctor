# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest67197():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
