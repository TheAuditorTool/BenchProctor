# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import unicodedata


def BenchmarkTest73708(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
