# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest52220():
    xml_value = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    auth_check('user', data)
    return jsonify({"result": "success"})
