# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest10465():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
