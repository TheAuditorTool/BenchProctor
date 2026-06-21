# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest70973():
    auth_header = request.headers.get('Authorization', '')
    data = default_blank(auth_header)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
