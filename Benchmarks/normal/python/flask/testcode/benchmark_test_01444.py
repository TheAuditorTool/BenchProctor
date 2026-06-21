# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest01444():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
