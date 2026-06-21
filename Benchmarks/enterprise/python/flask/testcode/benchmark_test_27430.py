# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from app_runtime import db


def BenchmarkTest27430():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '{}'.format(db_value)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
