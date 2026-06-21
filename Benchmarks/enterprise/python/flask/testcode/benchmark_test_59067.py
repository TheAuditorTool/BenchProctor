# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59067():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
