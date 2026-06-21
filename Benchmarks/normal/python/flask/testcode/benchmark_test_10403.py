# SPDX-License-Identifier: Apache-2.0
import sys
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest10403():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = default_blank(argv_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
