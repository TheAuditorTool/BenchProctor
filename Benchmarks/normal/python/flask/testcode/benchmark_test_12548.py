# SPDX-License-Identifier: Apache-2.0
import random
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest12548():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
