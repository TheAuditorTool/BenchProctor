# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40729():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
