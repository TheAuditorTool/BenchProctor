# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest60292():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
