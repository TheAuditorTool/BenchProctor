# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import defusedxml.ElementTree


def BenchmarkTest46351():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
