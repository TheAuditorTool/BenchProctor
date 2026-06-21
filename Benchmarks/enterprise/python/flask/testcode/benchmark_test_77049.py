# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77049():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
