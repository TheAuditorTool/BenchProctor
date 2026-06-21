# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest00406(path_param):
    path_value = path_param
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', path_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = path_value
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
