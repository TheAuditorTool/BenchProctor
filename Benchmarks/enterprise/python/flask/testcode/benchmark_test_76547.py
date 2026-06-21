# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest76547():
    env_value = os.environ.get('USER_INPUT', '')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not env_value.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(env_value)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
