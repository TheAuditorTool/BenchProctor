# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27916():
    host_value = request.headers.get('Host', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if host_value not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + host_value
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
