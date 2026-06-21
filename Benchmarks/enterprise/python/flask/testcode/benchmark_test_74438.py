# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74438():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
