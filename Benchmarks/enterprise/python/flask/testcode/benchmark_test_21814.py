# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import ast


def BenchmarkTest21814():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
