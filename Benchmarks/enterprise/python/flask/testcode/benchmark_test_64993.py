# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time
import ast
import subprocess


def BenchmarkTest64993():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
