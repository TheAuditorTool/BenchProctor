# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import ast


def BenchmarkTest02492():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    return render_template_string('safe block: {{ value }}', value=data)
