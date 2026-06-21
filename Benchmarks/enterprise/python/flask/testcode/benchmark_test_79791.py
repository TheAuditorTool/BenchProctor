# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79791():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
