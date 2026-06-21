# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest35540():
    env_value = os.environ.get('USER_INPUT', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if env_value not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + env_value
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
