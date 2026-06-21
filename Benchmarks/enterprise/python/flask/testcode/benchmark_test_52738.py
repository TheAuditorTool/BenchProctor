# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52738():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
