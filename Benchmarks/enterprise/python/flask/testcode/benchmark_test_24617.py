# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import ast


def BenchmarkTest24617():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    session['user'] = str(data)
    return jsonify({"result": "success"})
