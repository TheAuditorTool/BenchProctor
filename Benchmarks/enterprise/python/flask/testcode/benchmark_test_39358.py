# SPDX-License-Identifier: Apache-2.0
import random
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest39358():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
