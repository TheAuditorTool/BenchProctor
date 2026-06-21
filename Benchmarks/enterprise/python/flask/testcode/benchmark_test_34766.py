# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34766():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
