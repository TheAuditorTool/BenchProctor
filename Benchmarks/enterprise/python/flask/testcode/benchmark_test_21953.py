# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest21953(path_param):
    path_value = path_param
    data = default_blank(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
