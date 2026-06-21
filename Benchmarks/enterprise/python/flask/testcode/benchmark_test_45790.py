# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import ast
import urllib.parse


def BenchmarkTest45790():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
