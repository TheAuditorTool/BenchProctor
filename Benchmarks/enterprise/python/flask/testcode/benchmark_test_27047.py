# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27047():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
