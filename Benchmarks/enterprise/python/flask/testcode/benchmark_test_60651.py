# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import ast


def BenchmarkTest60651():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    processed = data[:64]
    return render_template_string(processed)
