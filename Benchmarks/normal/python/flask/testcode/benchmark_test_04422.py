# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import ast


def BenchmarkTest04422():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
