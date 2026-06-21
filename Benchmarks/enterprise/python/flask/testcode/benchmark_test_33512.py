# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest33512():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    digest = hashlib.pbkdf2_hmac('sha256', str(db_value).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
