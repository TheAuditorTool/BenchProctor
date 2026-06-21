# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest61874():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
