# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest43179(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
