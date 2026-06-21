# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify
import ast


def BenchmarkTest13576():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.post('http://api.prod.internal/data', data=str(processed))
    return jsonify({"result": "success"})
