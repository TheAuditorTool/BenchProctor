# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15902():
    user_id = request.args.get('id', '')
    if str(user_id) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
