# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54352():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    eval(str(data))
    return jsonify({"result": "success"})
