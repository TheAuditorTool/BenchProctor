# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
import unicodedata


def BenchmarkTest77858():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
