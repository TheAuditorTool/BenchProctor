# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request
import ast


def BenchmarkTest31646():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    processed = data[:64]
    return redirect(str(processed))
