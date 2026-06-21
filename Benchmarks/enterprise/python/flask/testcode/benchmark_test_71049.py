# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import ast
import requests


def BenchmarkTest71049():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.get('https://api.pycdn.io/data', params={'q': str(processed)}, verify=False)
    return jsonify({"result": "success"})
