# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54558():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
