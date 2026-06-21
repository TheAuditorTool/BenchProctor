# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57075():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
