# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import urllib.request


def BenchmarkTest12003():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
