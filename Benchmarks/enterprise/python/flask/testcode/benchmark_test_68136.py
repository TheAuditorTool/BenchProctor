# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68136():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
