# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest02509(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
