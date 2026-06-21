# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest43401(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    os.unlink(checked_path)
    return jsonify({"result": "success"})
