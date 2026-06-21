# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77723():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
