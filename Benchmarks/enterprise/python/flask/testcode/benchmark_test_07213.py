# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07213():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
