# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73691():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
