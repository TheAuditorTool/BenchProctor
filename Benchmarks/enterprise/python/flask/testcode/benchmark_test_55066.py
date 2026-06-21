# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55066():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
