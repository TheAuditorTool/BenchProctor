# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61251():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
