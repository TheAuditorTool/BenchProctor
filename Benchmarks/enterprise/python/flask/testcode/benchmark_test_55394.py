# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time
import ast


def BenchmarkTest55394():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
