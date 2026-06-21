# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify
import ast


def BenchmarkTest37433():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.post('http://api.prod.internal/data', data=str(processed))
    return jsonify({"result": "success"})
