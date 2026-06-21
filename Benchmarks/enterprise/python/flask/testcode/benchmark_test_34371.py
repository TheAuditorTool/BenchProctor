# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import ast
from app_runtime import db


def BenchmarkTest34371():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute('DELETE FROM accounts WHERE id = ?', (str(processed),))
    return jsonify({"result": "success"})
