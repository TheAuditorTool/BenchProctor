# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71583():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
