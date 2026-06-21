# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import defusedxml.ElementTree


def BenchmarkTest19253():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
