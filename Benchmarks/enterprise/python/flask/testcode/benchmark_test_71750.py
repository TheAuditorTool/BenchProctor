# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71750():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
