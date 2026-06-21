# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest46574():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
