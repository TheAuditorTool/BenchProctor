# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import ast


def BenchmarkTest65844():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    processed = str(data).replace("<script", "")
    return Markup('<img src="' + str(processed) + '">')
