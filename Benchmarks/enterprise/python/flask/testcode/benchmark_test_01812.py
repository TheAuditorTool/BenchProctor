# SPDX-License-Identifier: Apache-2.0
from flask import request
import ast


def BenchmarkTest01812():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    return str(data), 200, {'Content-Type': 'text/html'}
