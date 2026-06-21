# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01843():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
