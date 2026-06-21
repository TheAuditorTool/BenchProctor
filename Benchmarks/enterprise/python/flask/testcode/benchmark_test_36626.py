# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import ast
import socket


def BenchmarkTest36626():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return jsonify({"result": "success"})
