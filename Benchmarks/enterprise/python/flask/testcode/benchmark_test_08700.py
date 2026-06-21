# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import ast
import urllib.parse


def BenchmarkTest08700():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
