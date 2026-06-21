# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import ast


def BenchmarkTest73970():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
