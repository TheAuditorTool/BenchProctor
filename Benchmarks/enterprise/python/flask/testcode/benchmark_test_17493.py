# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17493():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    eval(str(data))
    return jsonify({"result": "success"})
