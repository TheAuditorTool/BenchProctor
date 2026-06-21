# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest42091():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
