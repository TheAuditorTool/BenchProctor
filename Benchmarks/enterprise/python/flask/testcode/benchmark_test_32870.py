# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32870():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
