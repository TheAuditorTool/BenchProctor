# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79244():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    eval(str(data))
    return jsonify({"result": "success"})
