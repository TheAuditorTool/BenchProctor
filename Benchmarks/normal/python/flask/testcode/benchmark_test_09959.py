# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest09959(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
