# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest65567(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    processed = data[:64]
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return jsonify({'record': str(record)}), 200
