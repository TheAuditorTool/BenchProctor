# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import ast


def BenchmarkTest31216():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    processed = data[:64]
    return render_template_string(processed)
