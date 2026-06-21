# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32315():
    user_id = request.args.get('id', '')
    if str(user_id).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
