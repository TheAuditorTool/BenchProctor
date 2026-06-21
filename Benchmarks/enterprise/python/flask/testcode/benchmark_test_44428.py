# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest44428():
    stdin_value = input('input: ')
    data = '%s' % (stdin_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return content
