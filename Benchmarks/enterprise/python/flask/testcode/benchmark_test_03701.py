# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest03701():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not db_value.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(db_value)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
