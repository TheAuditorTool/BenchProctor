# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest09110():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
