# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast


def BenchmarkTest39356():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    os.seteuid(65534)
    return jsonify({"result": "success"})
