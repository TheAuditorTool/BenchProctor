# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest59141(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
