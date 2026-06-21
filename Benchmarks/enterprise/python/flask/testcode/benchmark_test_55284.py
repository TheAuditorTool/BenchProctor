# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest55284():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
