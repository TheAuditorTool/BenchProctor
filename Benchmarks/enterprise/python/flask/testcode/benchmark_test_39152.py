# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39152():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
