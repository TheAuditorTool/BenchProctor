# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast


def BenchmarkTest28375():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    os.remove(str(data))
    return jsonify({"result": "success"})
