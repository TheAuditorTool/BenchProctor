# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import ast
import urllib.parse


def BenchmarkTest74068():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
