# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46441():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
