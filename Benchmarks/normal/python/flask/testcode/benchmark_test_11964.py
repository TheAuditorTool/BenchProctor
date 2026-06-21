# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import os


def BenchmarkTest11964(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
