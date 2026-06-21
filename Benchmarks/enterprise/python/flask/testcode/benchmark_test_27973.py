# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27973():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
