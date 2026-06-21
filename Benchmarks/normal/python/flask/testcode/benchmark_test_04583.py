# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import ast


def BenchmarkTest04583():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    def _primary():
        subprocess.run('echo ' + str(data), shell=True)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
