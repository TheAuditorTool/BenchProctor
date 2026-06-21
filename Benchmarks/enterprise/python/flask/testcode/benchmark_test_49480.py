# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import ast


def BenchmarkTest49480():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
