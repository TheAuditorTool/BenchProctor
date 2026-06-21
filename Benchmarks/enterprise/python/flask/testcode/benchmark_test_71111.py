# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import ast


def BenchmarkTest71111():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
