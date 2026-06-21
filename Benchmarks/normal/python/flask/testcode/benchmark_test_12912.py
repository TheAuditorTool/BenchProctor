# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import ast
import socket


def BenchmarkTest12912():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
