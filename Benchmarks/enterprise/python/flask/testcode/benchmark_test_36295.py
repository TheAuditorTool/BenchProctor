# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import ast


def BenchmarkTest36295():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})
