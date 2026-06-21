# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest26823(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
