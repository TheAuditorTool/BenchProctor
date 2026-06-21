# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import ast


def BenchmarkTest04690():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    def _primary():
        return render_template_string(data)
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
