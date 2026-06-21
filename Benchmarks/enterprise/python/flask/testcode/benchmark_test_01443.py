# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01443():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
