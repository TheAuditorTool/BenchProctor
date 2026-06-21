# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70176():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
