# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast


def BenchmarkTest05031():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
