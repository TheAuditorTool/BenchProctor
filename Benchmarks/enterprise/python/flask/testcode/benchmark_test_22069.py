# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import ast


def BenchmarkTest22069():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
