# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import pickle


def BenchmarkTest18744():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    eval(compile("pickle.loads(data.encode('latin-1'))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
