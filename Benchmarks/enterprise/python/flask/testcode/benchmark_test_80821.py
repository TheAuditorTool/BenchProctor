# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import ast


def BenchmarkTest80821():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
