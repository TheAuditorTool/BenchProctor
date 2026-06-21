# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04009():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
