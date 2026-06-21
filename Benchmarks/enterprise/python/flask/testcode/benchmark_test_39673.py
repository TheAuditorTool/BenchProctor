# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify
import ast


def BenchmarkTest39673():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
