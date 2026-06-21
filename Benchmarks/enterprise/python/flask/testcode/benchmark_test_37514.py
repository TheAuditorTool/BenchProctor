# SPDX-License-Identifier: Apache-2.0
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest37514():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
