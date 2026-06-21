# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import ast


def BenchmarkTest70495():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    if str(data).lower() not in ('true', 'false'):
        return jsonify({'error': 'invalid boolean'}), 400
    session['user'] = str(data)
    return jsonify({"result": "success"})
