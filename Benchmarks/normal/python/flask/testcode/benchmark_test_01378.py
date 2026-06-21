# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request
import ast


def BenchmarkTest01378():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    processed = data[:64]
    return redirect(str(processed))
