# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import ast


def BenchmarkTest24915():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
