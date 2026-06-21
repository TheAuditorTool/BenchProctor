# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81005():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    eval(str(data))
    return jsonify({"result": "success"})
