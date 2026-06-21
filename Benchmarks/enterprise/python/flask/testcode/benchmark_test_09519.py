# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import tempfile
from app_runtime import db


def BenchmarkTest09519():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
