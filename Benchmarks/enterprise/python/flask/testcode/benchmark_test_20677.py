# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import ast


def BenchmarkTest20677():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
