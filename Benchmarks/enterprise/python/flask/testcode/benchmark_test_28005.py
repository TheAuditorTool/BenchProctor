# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from app_runtime import db


def BenchmarkTest28005():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    random.seed(int(db_value) if str(db_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
