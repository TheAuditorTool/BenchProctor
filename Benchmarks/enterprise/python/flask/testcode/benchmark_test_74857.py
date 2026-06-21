# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import ast
import urllib.parse


def BenchmarkTest74857():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
