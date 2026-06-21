# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42014():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
