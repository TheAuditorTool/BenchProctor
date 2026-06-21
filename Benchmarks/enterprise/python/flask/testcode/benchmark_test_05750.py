# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify
import ast


def BenchmarkTest05750():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<script src="' + str(processed) + '"></script>', 200, {'Content-Type': 'text/html'}
