# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest03612():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
