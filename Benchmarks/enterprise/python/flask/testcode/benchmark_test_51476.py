# SPDX-License-Identifier: Apache-2.0
from flask import request
import ast


def BenchmarkTest51476():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
