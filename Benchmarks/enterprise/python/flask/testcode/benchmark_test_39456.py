# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest39456(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
