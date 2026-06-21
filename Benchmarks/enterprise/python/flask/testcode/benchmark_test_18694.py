# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18694():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    eval(str(data))
    return jsonify({"result": "success"})
