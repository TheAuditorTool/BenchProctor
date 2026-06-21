# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import ast


def BenchmarkTest73318():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data).startswith(('10.', '192.168.', '127.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
