# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01029():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
