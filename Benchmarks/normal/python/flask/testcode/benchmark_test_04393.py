# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest04393():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(db_value),))
    return jsonify({'secret': str(secret)}), 200
