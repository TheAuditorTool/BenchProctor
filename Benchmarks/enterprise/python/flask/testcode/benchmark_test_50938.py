# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest50938(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
