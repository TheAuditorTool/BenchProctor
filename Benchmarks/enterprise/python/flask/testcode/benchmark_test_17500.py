# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import ast


def BenchmarkTest17500():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
