# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00938():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    eval(str(data))
    return jsonify({"result": "success"})
