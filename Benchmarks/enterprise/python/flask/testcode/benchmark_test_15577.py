# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15577():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
