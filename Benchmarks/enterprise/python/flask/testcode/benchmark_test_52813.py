# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest52813():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
