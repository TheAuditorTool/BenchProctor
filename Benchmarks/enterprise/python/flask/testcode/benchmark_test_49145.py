# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
import ast


def BenchmarkTest49145():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
