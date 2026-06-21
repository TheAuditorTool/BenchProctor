# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31906():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
