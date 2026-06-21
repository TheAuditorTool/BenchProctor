# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest10598():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
