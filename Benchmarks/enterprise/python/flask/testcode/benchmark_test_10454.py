# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10454():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
