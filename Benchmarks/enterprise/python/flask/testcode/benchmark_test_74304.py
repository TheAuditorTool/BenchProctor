# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify
import ast


def BenchmarkTest74304():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<script src="' + str(processed) + '"></script>', 200, {'Content-Type': 'text/html'}
