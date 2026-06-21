# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import ast


def BenchmarkTest15249():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
