# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79761():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
