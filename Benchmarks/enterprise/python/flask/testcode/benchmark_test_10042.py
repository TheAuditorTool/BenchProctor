# SPDX-License-Identifier: Apache-2.0
from flask import request
import ast


def BenchmarkTest10042():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
