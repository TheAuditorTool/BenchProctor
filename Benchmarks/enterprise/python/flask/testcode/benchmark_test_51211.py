# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest51211():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(db_value))
    return jsonify({"result": "success"})
