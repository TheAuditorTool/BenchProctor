# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast
import subprocess


def BenchmarkTest57400():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    eval(compile("subprocess.run([str(data), '--status'], shell=False)", '<sink>', 'exec'))
    return jsonify({"result": "success"})
