# SPDX-License-Identifier: Apache-2.0
import random
import re
from flask import request, jsonify
import ast


def BenchmarkTest71670():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
