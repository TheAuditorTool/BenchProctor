# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18850():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
