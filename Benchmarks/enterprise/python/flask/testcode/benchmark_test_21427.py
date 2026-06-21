# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast
import subprocess


def BenchmarkTest21427():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
