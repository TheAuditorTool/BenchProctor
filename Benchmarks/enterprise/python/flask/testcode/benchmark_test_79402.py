# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import ast


def BenchmarkTest79402():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    session['data'] = str(data)
    return jsonify({"result": "success"})
