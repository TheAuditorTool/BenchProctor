# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest69142():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
