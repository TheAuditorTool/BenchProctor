# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18283():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
