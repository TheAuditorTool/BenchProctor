# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61582():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    int(str(data))
    return jsonify({"result": "success"})
