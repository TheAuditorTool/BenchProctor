# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42298():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    eval(str(data))
    return jsonify({"result": "success"})
