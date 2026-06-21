# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import ast


def BenchmarkTest78387():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
