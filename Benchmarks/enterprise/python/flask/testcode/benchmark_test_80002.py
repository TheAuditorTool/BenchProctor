# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import ast


def BenchmarkTest80002():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    processed = data[:64]
    session['data'] = str(processed)
    return jsonify({"result": "success"})
