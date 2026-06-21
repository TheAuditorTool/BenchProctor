# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify


def BenchmarkTest09651():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
