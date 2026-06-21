# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import ast


def BenchmarkTest41840():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
