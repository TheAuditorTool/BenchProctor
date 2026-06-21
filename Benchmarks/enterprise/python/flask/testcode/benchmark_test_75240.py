# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast
import subprocess


def BenchmarkTest75240():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
