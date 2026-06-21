# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest05786(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
