# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest61783():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    processed = 'true' if str(db_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return jsonify({"result": "success"})
