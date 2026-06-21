# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest52346():
    xml_value = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    return jsonify({'error': 'An internal error occurred'}), 500
