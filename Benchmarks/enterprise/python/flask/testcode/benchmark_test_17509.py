# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import ast


def BenchmarkTest17509():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
