# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import importlib


def BenchmarkTest25042():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})
