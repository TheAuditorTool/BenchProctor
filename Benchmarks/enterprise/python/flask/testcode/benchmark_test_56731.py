# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56731():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    eval(str(data))
    return jsonify({"result": "success"})
