# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest79478(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
