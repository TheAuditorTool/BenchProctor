# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import ast


def BenchmarkTest19856():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
