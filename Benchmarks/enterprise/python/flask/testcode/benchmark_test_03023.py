# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest03023():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
