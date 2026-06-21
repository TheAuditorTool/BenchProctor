# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import ast


def BenchmarkTest05497():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
