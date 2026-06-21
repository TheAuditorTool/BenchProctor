# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29495():
    cookie_value = request.cookies.get('session_token', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if cookie_value not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + cookie_value
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
