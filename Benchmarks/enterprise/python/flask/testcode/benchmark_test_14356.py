# SPDX-License-Identifier: Apache-2.0
import hashlib
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest14356():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
