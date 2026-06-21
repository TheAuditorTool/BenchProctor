# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24174():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    eval(str(data))
    return jsonify({"result": "success"})
