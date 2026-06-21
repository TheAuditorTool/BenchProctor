# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest11768():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
