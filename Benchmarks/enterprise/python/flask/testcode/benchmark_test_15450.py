# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15450():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
