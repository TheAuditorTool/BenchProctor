# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import ast


def BenchmarkTest39209():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
