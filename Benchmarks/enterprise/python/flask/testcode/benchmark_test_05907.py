# SPDX-License-Identifier: Apache-2.0
import re
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest05907(path_param):
    path_value = path_param
    data = unquote(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
