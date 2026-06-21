# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06123():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
