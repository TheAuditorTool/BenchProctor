# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest08706():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})
