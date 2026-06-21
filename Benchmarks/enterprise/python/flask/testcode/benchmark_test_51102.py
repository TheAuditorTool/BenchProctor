# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest51102():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
