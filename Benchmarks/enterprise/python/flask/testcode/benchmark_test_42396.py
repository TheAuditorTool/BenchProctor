# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from app_runtime import db


def BenchmarkTest42396():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
