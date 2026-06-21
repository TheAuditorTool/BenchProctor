# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import ast


def BenchmarkTest70011():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
