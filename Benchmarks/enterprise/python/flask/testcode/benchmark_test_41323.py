# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41323():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
