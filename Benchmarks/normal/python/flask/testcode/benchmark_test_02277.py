# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import ast


def BenchmarkTest02277():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
