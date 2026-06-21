# SPDX-License-Identifier: Apache-2.0
import os
import re
import sys
from flask import jsonify


def BenchmarkTest57581():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    parts = []
    for token in str(argv_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
