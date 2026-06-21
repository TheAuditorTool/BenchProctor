# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
import ast


def BenchmarkTest08715():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
