# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import ast


def BenchmarkTest29287():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
