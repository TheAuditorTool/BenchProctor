# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13091():
    auth_header = request.headers.get('Authorization', '')
    exec(str(auth_header))
    return jsonify({"result": "success"})
