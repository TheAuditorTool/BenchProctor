# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42602():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
