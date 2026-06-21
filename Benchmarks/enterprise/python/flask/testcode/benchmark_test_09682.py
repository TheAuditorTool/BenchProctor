# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import defusedxml.ElementTree


def BenchmarkTest09682():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
