# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import ast


def BenchmarkTest68379():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    _ev = {}
    eval(compile('_ev[\'r\'] = Markup(\'<img src="\' + str(data) + \'">\')', '<sink>', 'exec'))
    return _ev['r']
