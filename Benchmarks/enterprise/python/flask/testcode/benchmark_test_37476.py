# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37476():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
