# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18086():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
