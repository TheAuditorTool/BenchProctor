# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import ast


def BenchmarkTest73463():
    xml_value = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
