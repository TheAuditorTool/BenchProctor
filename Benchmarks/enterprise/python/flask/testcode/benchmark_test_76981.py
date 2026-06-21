# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76981():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
