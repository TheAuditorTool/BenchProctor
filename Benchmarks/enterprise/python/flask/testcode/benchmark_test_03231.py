# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03231():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
