# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
from app_runtime import db


def BenchmarkTest03364():
    xml_value = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
