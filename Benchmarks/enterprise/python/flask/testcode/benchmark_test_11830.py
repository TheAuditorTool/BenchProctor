# SPDX-License-Identifier: Apache-2.0
import sys
from flask import jsonify
import json


def BenchmarkTest11830():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    try:
        data = json.loads(argv_value).get('value', argv_value)
    except (json.JSONDecodeError, AttributeError):
        data = argv_value
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return content
