# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import ast


def BenchmarkTest31758():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
