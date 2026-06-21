# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39557():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
