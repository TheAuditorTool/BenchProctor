# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest08912(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
