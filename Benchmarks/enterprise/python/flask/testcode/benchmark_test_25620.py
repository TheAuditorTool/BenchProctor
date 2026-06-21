# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest25620(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
