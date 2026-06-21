# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54722():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
