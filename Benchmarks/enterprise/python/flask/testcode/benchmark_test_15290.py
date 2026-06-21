# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import defusedxml.ElementTree


def BenchmarkTest15290():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
