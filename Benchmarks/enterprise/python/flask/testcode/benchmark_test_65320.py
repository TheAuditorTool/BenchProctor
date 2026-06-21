# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest65320():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    auth_check('user', processed)
    return jsonify({"result": "success"})
