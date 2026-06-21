# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55973():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    int(str(data))
    return jsonify({"result": "success"})
