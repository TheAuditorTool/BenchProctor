# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
import tempfile
from app_runtime import db


def BenchmarkTest48590():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
