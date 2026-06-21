# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42697():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
