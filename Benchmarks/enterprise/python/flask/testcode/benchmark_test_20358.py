# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest20358():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
