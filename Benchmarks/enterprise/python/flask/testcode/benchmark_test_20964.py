# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest20964():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    trusted_claim = str(db_value)
    return jsonify({'trusted': trusted_claim}), 200
